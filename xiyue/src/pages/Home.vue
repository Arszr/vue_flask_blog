<!--
 * @Description: In User Settings Edit
 * @Author: your name
 * @Date: 2019-10-01 00:40:17
 * @LastEditTime: 2019-10-12 20:06:29
 * @LastEditors: Please set LastEditors
 -->

<!-- 首页 -->
<template>
  <div>
    <xy-nav></xy-nav>
    <div class="container">
      <el-row :gutter="30">
        <el-col :sm="24" :md="16" style="transition:all .5s ease-out;margin-bottom:30px;">
          <xy-sharelist></xy-sharelist>
        </el-col>
        <el-col :sm="24" :md="8">
          <xy-rightlist></xy-rightlist>
        </el-col>
      </el-row>
    </div>
    <xy-footer></xy-footer>
  </div>
</template>

<script>
import header from "../components/header.vue";
import footer from "../components/footer.vue";
import ShareList from "../components/ShareList.vue";
import RightList from "../components/RightList.vue";
import LeftTime from "../components/LeftTime.vue";
export default {
  name: "Home",
  data() {
    //选项 / 数据
    return {};
  },
  methods: {
    //事件处理器
  },
  components: {
    //定义组件
    "xy-nav": header,
    "xy-sharelist": ShareList,
    "xy-lefttime": LeftTime,
    "xy-rightlist": RightList,
    "xy-footer": footer
  },
  created() {
    //生命周期函数
  }
};
</script>

<style>
</style>
