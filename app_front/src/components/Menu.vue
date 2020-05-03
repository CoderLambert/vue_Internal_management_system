<template>
      <el-menu
        :default-active="activeIndex"
        @select="handleSelect"
        background-color=#333744
        text-color=#fff
        active-text-color="skyblue"
        :unique-opened = true
        :collapse="isCollapse"
        :collapse-transition = false
        router
        >
        <template
          v-for="menu in menu_list"
        >
          <el-submenu
            :index="menu.path"
            v-bind:key="menu.id"
            v-if = "menu.sub_menu !== null"
          >
            <template slot="title">
              <i :class="menu.icon"></i>
              <span slot="title">{{menu.name}}</span>
            </template>
            <el-menu-item
              v-for="sub_menu in menu.sub_menu"
              :index="sub_menu.path"
              v-bind:key="sub_menu.id"
            >
              <i :class="sub_menu.icon"></i> {{sub_menu.name}}
            </el-menu-item>
          </el-submenu>

          <el-menu-item
            :index="menu.path"
            v-bind:key="menu.id"
            v-if = "menu.sub_menu === null"
          >
            <i :class="menu.icon"></i>
            <span>
             {{menu.name}}
             </span>
          </el-menu-item>

        </template>

      </el-menu>

</template>

<script>

export default {
  name: 'Menu',
  props: ['isCollapse'],
  data () {
    return {
      activeIndex: '/',
      menu_list: [
        { id: 0,
          name: '首页',
          path: '/',
          icon: 'el-icon-s-home',
          sub_menu: null
        },

        { id: 1,
          name: '镜像管理',
          path: '/image',
          icon: 'el-icon-s-cooperation',
          sub_menu: [
            { id: 11, name: '文件信息', path: '/image/info', icon: 'el-icon-s-cooperation' },
            { id: 12, name: '上传镜像', path: '/image/upload', icon: 'el-icon-upload' }
          ]
        },

        { id: 2,
          name: '项目管理',
          path: '/project',
          icon: 'el-icon-s-platform',
          sub_menu: [
            { id: 11, name: '项目信息', path: '/project/info', icon: 'el-icon-s-order' },
            { id: 12, name: '机器信息', path: '/project/machine/info', icon: 'el-icon-s-order' }
            // { id: 13, name: 'SVN 信息', path: '/project/svn', icon: 'el-icon-s-order' }
          ]
        },
        // { id: 3,
        //   name: '开发',
        //   path: '/development',
        //   icon: 'el-icon-document',

        //   sub_menu: [
        //     { id: 31, name: '功能列表', path: '/development/function', icon: 'el-icon-s-cooperation' },
        //     { id: 32, name: '时间线', path: '/development/timeline', icon: 'el-icon-s-cooperation' }

        //   ]
        // },
        // { id: 4,
        //   name: '用户',
        //   path: '/user',
        //   icon: 'el-icon-document',
        //   sub_menu: [
        //     { id: 41, name: '用户信息', path: '/user/info', icon: 'el-icon-s-cooperation' },
        //     { id: 42, name: '用户权限管理', path: '/user/privilage', icon: 'el-icon-s-cooperation' }
        //   ]
        // },

        { id: 5,
          name: '文章管理',
          path: '/article',
          icon: 'el-icon-document',
          sub_menu: [
            // { id: 51, name: '富文本', path: '/article/rich', icon: 'el-icon-s-cooperation' },
            { id: 51, name: '文章总览', path: '/articles/', icon: 'el-icon-s-cooperation' },
            { id: 52, name: '添加文章', path: '/article/add/markdown', icon: 'el-icon-s-cooperation' },
            { id: 53, name: '笔记本', path: '/articles/notes', icon: 'el-icon-s-cooperation' },
            { id: 54, name: '文章分类', path: '/articles/types', icon: 'el-icon-s-cooperation' }
          ]
        },
        { id: 6,
          name: '导航',
          path: '/navigation',
          icon: 'el-icon-document',
          sub_menu: [
            { id: 61, name: '常用网站', path: '/navigation/webside', icon: 'el-icon-s-cooperation' },
            { id: 62, name: '网站分类', path: '/navigation/webtype', icon: 'el-icon-s-cooperation' }
            // { id: 63, name: '资源', path: '/navigation/resource', icon: 'el-icon-s-cooperation' }
          ]
        },
        { id: 7,
          name: '反馈',
          path: '/suggest',
          icon: 'el-icon-document',
          sub_menu: [
            { id: 71, name: '需求', path: '/suggest/demand', icon: 'el-icon-s-cooperation' }
            // { id: 72, name: '添加需求', path: '/suggest/demand/add', icon: 'el-icon-s-cooperation' }

          ]
        }

      ]
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      // console.log(key, keyPath);
      this.activeIndex = key
    }

  }
}
</script>

<style lang="less" scoped>

</style>
