<template>
<div>
  user
</div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'home',
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

  },
  components: {
  }
}
</script>

<style lang="less" scoped>

</style>
