<template>
    <div>
              <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="购买页面"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed="true"
      >
      </van-nav-bar>
      <van-row>
          
      </van-row>
    </div>
</template>
<script>
export default {
    date(){
        return {

        }
    },
    methods: {
            onClickLeft() {
      this.$router.push("/Good");
    }
    },
}
</script>