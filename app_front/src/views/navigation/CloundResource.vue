<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>导航</el-breadcrumb-item>
      <el-breadcrumb-item>云资源</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card-box">    
    </el-card>

  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'CloundResource',
  data () {
    return {
    }
  },
  computed: {
  },
  mounted () {
  },
  beforeDestroy () {
  },

  methods: {

  },
  components: {

  }
}
</script>

<style lang="less" scoped>

</style>
