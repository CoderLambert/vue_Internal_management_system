<template>
  <div>
    <!-- 调用组件  -->
    <draggable element="ul" v-model="list">
      <li v-for="(item, index) in list" v-bind:key="index">{{item.name}}</li>
    </draggable>
    <!-- 输出list数据 -->
    {{list}}
  </div>
</template>

<script>
// 引入拖拽组件
import draggable from 'vuedraggable'
export default {
  name: 'demo',
  components: {
    draggable
  },
  data () {
    return {
      list: [
        {
          id: 1,
          name: 'a'
        },
        {
          id: 2,
          name: 'b'
        },
        {
          id: 3,
          name: 'c'
        },
        {
          id: 4,
          name: 'd'
        },
        {
          id: 5,
          name: 'e'
        },
        {
          id: 6,
          name: 'f'
        }
      ]
    }
  }
}
</script>
