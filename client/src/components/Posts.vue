<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Posts</h1>
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
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
        <br><br>
        <button type="button" class="btn btn-primary">Add Post</button>
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
    };
  },
  methods: {
    getPosts() {
      const path = 'http://localhost:5000/api/posts/';
      axios.get(path)
        .then((res) => {
          this.posts = res.data;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getPosts();
  },
};
</script>
