<template>
  <div>
    <ul class="list-item" v-for="(item, index) in ArticaleTypeList" :key="index">
        <li class="item-name">
            <el-checkbox :label="item.id" @change="handleChange"> {{item.name}} </el-checkbox>
        </li>
        <ArticaleTypeTree v-if="item.children" class="children-item" :ArticaleTypeList="item.children"></ArticaleTypeTree>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'ArticaleTypeTree',
  props: ['ArticaleTypeList'],
  data () {
    return {
      checkList: []
    }
  },
  methods: {
    getAllNode () {
      console.log(this.$refs.type_tree.getCheckedKeys())
    },
    handleChange (value) {
      console.log(value)
    }

  },
  computed: {},
  watch: {
    filterText (val) {
      this.$refs.type_tree.filter(val)
    }
  }
}
</script>

<style lang="less" scoped>
.list-item {
  list-style: none;
  padding-inline-start: 25px;
}
</style>
