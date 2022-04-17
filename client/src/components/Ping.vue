<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Posts</h1>

            <form @submit.prevent="getPosts">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" v-model="query">
                </div>
                <div class="control">
                    <button class="button is-success">Search</button>
                </div>
              </div>
            </form>
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
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>

                <div class="buttons">
                    <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
                    <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Next</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data() {
    return {
      posts: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      num_posts: 0
    }
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
          .get(`http://localhost:5000/api/posts/?page=${this.currentPage}`)
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
    }
  }
}
</script>
