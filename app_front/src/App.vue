<template>
  <div id="app">
    <!-- <router-view></router-view> -->
    <!-- <transition  name="transitionRouter" mode="out-in"> -->
      <router-view></router-view>
    <!-- </transition> -->
    <!-- keep alive 原理是啥 -->
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  }
}
</script>

<style>
.v-show-content {
  background: #fff;
}

.transitionRouter-enter-active, .transitionRouter-leave-active {
    transition: all 0.4s;
} .transitionRouter-enter, .transitionRouter-leave{
    transform: translate3d(100%, 0, 0);
}
</style>
