<template>
  <div>
    <p>Это какой-то {{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
