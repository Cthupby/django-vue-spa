<template>
  <div class="container">
      <div class="col">
        <div class="row align-items-start mb-2">
          <h1 class="text-primary">Django Vue Single Page Application</h1>
          <h4>Список постов:</h4>
          <hr><br><br>
          <div class="container">
            <div class="col">
              <div class="input-group mx-12 mb-3">
                <select class="form-select form-select">
                  <option selected>Выберите колонку для фильтрации</option>
                  <option v-on:click="column = 'title'">Название</option>
                  <option v-on:click="column = 'amount'">Количество</option>
                  <option v-on:click="column = 'distance'">Расстояние</option>
                </select>
                <select class="form-select form-select">
                  <option selected>Выберите условие для фильтрации</option>
                  <option v-on:click="condition = '__iexact'">Равно</option>
                  <option v-on:click="condition = '__icontains'">Содержит</option>
                  <option v-on:click="condition = '__gt'">Больше</option>
                  <option v-on:click="condition = '__lt'">Меньше</option>
                </select>
                <input type="text"
                       class="form-control"
                       placeholder="Поиск"
                       v-model="query"
                       aria-label="Search">
                  <div class="input-group-append">
                    <button class="btn btn-primary"
                            v-on:click.prevent="getPosts()"">Поиск</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Дата</th>
              <th scope="col">Название</th>
              <th scope="col">Количество</th>
              <th scope="col">Расстояние</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post in posts">
              <td>{{ post.date }}</td>
              <td>{{ post.title }}</td>
              <td>{{ post.amount }}</td>
              <td>{{ post.distance }}</td>
            </tr>
          </tbody>
        </table>
        <br><br>  
      <div class="row align-items-end">
        <ul class="pagination">
          <li class="page-item ">
            <button class="btn btn-primary"
                    @click="goToPreviousPage()"
                    :disabled="showNextButton">Previous page</button>
          </li>
          <li class="page-item">
            <button class="btn btn-primary"
                    @click="goToNextPage()"
                    :disabled="showPreviousButton">Next page</button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      posts: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: '',
      column: '',
      condition: '',
      num_posts: 0
    };
  },
  mounted() {
    this.getPosts()
  },
  methods: {
    goToNextPage() {
      this.currentPage += 1
      this.getPosts()
    },
    goToPreviousPage() {
      this.currentPage -= 1
      this.getPosts()
    },
    async getPosts() {
      this.showNextButton = false
      this.showPreviousButton = false
      await axios
        .get(`http://localhost:5000/api/posts/`)
          .then(response => {
            console.log(response.data)
            this.num_posts = response.data.count
          })
      await axios
        .get(`http://localhost:5000/api/posts/?page=${this.currentPage}&${this.column}${this.condition}=${this.query}`)
        .then(response => {
        this.posts = response.data.results
          if (response.data.next) {
          this.showNextButton = true
          }
          if (response.data.previous) {
          this.showPreviousButton = true
          }
        })
        .catch(error => {
          console.log(error)
      })
    },
  },
};
</script>
