<template>
    <el-container>
      <el-header>
        <div class="logo">
          <span class="logo-title">Beyond PLM</span>
        </div>
        <div class="user-info">
            <a :href="api_link" v-if="username=='lambert'" target="_blank" >管理站点</a>
            <a :href="doc_link" v-if="username=='lambert'" target="_blank" >api 文档</a>

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
            <!-- <el-backtop target=".cs-bottom" :bottom="100">
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
              
               <i class="el-icon-top"></i> -->
              <!-- 到达底部
             </div>
            </el-backtop> --> 

            <el-backtop target=".el-main" :bottom="100">
              <div
                style="{
                  height: 150px;
                  width: 200px;
                  background-color: #f2f5f6;
                  box-shadow: 0 0 6px rgba(0,0,0, .12);
                  text-align: center;
                  line-height: 30px;
                  color: #1989fa;
                  border 1px solid
                }"
              >
              返回顶部
             </div>
            </el-backtop>

          </template>
        </el-main>
      </el-container>

      <div style="display:hide" class="cs-bottom"> </div>
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
      username: sessionStorage.getItem('username'),
      doc_link: `http://${window.location.host}/docs/`,
      api_link: `http://${window.location.host}/admin/`
    }
  },
  computed: {
  },
  mounted () {
     document.addEventListener('keydown', this.handleEvent)
  },
  beforeDestroy () {
  },

  methods: {
    handleEvent (event) {
      // console.log(event.keyCode)
      if ((event.keyCode === 66 || event.keyCode === 98 ) && event.ctrlKey) {
        // console.log('拦截到37')
        this.toogleCollapse()
      }
    },
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
  .el-backtop{
    z-index: 9999;
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
    // overflow-y: scroll;
    // &::-webkit-scrollbar {
    //     /*滚动条整体样式*/
    //     width: 2px;
    //     /*高宽分别对应横竖滚动条的尺寸*/
    //     height: 4px;
    // }

    // &::-webkit-scrollbar-thumb {
    //     /*滚动条里面小方块*/
    //     border-radius: 5px;
    //     height: 60px;
    //     -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    //     background: #333744;
    // }

    // &::-webkit-scrollbar-track {
    //     /*滚动条里面轨道*/
    //     -webkit-box-shadow: inset 0 0 5px rgb(255, 255, 255);
    //     border-radius: 0;
    //     background: rgba(0, 0, 0, 0.1);
    // }
  }
  .el-main{
    background-color: #EAEDF1;
    margin: 0;
    padding: 20px;
    overflow-y: scroll;
    &::-webkit-scrollbar {
        /*滚动条整体样式*/
        width: 8px;
        /*高宽分别对应横竖滚动条的尺寸*/
        height: 4px;
    }

    &::-webkit-scrollbar-thumb {
        /*滚动条里面小方块*/
        border-radius: 5px;
        -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
        background: rgba(0, 0, 0, 0.2);
    }

    &::-webkit-scrollbar-track {
        /*滚动条里面轨道*/
        -webkit-box-shadow: inset 0 0 5px rgb(255, 255, 255);
        border-radius: 0;
        background: rgba(0, 0, 0, 0.1);
    }

  }
/* To style the document scrollbar, remove `.custom-scrollbar` */
// .el-main::-webkit-scrollbar {
//   width: 8px;
// }
// .el-main::-webkit-scrollbar-track {
//   box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
//   border-radius: 10px;
// }
// .el-main::-webkit-scrollbar-thumb {
//   border-radius: 10px;
//   box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.5);
// }

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
