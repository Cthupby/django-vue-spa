<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="row mb-2">
        <h1>Posts</h1>
        </div>
        <hr><br><br>
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
        
        <div class="col">
        	
        	<ul class="pagination justify-content-center">
						<li class="page-item">
							<button class="btn btn-primary" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
						</li>

						<li class="page-item">
							<button class="btn btn-primary" @click="goToNextPage()" v-if="showNextButton">Next</button>
						</li>
					</ul>
        
        </div>
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
    },
  },
};
</script>
