<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: "Ping",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    async getMessage() {
      const result = await this.$http.get("ping");
      const { data: res } = await this.$http.get("ping");
      // console.log(result);
      // console.log(result.status)
      this.msg = res;
    }
  },
  created() {
    this.getMessage();
  }
};
</script>