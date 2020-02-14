<template>
    <el-container>
      <el-header>
        <div class="logo">
          <span class="logo-title">Beyond PLM</span>
        </div>
        <div class="user-info">
            <a href="http://127.0.0.1:9200/admin/" v-if="username=='lambert'" target="_blank" >管理站点</a>
            <a href="http://127.0.0.1:9200/docs" v-if="username=='lambert'" target="_blank" >api 文档</a>

          <span class="user-info-name">当前用户: {{ username }}</span>
          <el-button type="user-info-logout" @click="logout">
            退出
          </el-button>
        </div>
      </el-header>
      <el-container>
        <el-aside :width="this.asideWidth">
          <div class="toogle-button" @click="toogleCollapse">|||</div>
          <Menu  v-bind:isCollapse="this.isCollapse "></Menu>
        </el-aside>
        <el-main>        <!--路由占位符-->
        <router-view>
          </router-view>
          <template>
            <el-backtop target=".el-main" :bottom="100">
              <div
                style="{
                  height: 150px;
                  width: 150px;
                  background-color: #f2f5f6;
                  box-shadow: 0 0 6px rgba(0,0,0, .12);
                  text-align: center;
                  line-height: 40px;
                  color: #1989fa;
                  border 1px solid
                }"
              >

              <i class="el-icon-top"></i>

             </div>
            </el-backtop>
          </template>
        </el-main>
      </el-container>
    </el-container>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu'
export default {
  name: 'Index',
  data () {
    return {
      asideWidth: '200px',
      isCollapse: false,
      username: sessionStorage.getItem('username')
    }
  },
  computed: {
  },
  mounted () {

  },
  beforeDestroy () {
  },

  methods: {
    logout () {
      sessionStorage.clear()
      this.$router.push({ name: 'login' })
      this.$message.info('当前登录用户已退出')
    },

    toogleCollapse () {
      this.isCollapse = !this.isCollapse
      this.asideWidth = this.isCollapse ? '64px' : '200px'
    }
  },
  components: {
    Menu
  }
}
</script>

<style lang="less" scoped>
  .el-container{
    height: 100%;
  }
  .el-header{
    background-color: #373D41;
    display: flex;
    justify-content: space-between;
    align-items: center;
    .logo{
      .logo-title{
        color: #EAEDF1;
        font-size: 30px;
      }
    }
    .user-info{
      .user-info-name{
        font-size:18px;
        margin: 0 20px;
        color:#fff
      }
      a{
        cursor: pointer;
        color: skyblue;
        text-decoration: none;
        font-size: 20px;
        margin-right: 20px;
      }
    }
  }
  .el-aside{
    background-color: #333744;
    // height: 100vh;
  }
  .el-main{
    background-color: #EAEDF1;
    margin: 0;
    padding: 20px;
    overflow-y: scroll;
  }
  .el-menu{
    border: 0
  }
  .toogle-button{
    color: #fff;
    font-size: 12px;
    text-align: center;
    line-height: 25px;
    background-color: #4a5064;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    cursor: pointer;
    letter-spacing: .1em;
  }
</style>
