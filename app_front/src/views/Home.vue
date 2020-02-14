<template>
  <div class="home">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>

    </el-breadcrumb>
    <el-card class="box-card-box">

      <el-carousel height='500px' :autoplay='enableAutoplay' arrow="always">
        <el-carousel-item v-for="item in carousel_info" :key="item">
          <h3>{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>
    </el-card>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'index',
  data () {
    return {
      enableAutoplay: true,
      carousel_info: [
        '用户注册/登录功能: 已完成',
        '镜像文件功能: 已完成上传、显示、查询、修改文件信息、下载、删除功能',
        '项目信息功能: 已完成新建、显示、查询、复制 SVN 信息 到粘贴板功能',
        '机器信息功能：已完成新建、显示、查询、复制 Web 信息到粘贴板、跳转 BMC Web功能'
      ]
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

  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    // margin: 0 auto;
    text-align: center;

  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
