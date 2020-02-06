<template>
  <div class="home">
    <el-button type="info" @click="logout">
      退出
    </el-button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  methods: {
    logout () {
      sessionStorage.clear()
      this.$router.push({ name: 'login' })
      this.$message.info('当前登录用户已退出')
    }
  },
  components: {
  }
}
</script>
