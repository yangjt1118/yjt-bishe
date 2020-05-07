<template>
  <div>
    <van-dialog
      v-model="show"
      title="购买支付"
      show-cancel-button
      :beforeClose="beforeClose"
    >
      <van-cell title="商品">{{ good.name }}</van-cell>
      <van-cell title="价格">{{ good.price }}</van-cell>
      <van-field
        readonly
        clickable
        name="picker"
        :value="value"
        label="卡号"
        placeholder="选择卡号"
        @click="showPicker = true"
      />
      <van-popup v-model="showPicker" position="bottom">
        <van-picker
          show-toolbar
          :columns="columns"
          @confirm="onConfirm"
          @cancel="showPicker = false"
        />
      </van-popup>
      <van-field
        v-model="good.paypassword"
        type="password"
        name="支付密码"
        label="支付密码"
        placeholder="支付密码"
        :rules="[{ required: true, message: '请填写支付密码' }]"
      />
    </van-dialog>
    <div style="margin-bottom:50px" v-if="goodshow==true">
      <div v-for="(item, index) in tagitems" :key="index">
        <van-col span="4"
          ><van-button plain hairline type="primary" size="small">{{
            item.tag_name
          }}</van-button></van-col
        >
      </div>
      <van-card
        :price="item.price"
        :desc="item.description"
        :title="item.name"
        :thumb="item.image"
        v-for="(item, index) in items"
        :key="index"
        class="good1"
      >
        <template #footer>
          <van-button size="mini" type="info" @click="tobuy(index)"
            >立即购买</van-button
          >
          <van-button size="mini" type="danger" @click="move(index)"
            >不感兴趣</van-button
          >
        </template>
      </van-card>
    </div>
    <div style="color:#999999;width:100%;height: 30%;text-align: center;line-height: 190px;" v-else>暂时没有发布的商品</div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      items: {},
      tagitems: {},
      user2: {},
      show: false,
      user: {},
      good: {},
      value: "",
      columns: [],
      showPicker: false,
      goodshow:false
    };
  },
  mounted() {
    this.fench();
    // this.fench1()
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      if (this.user2 == null) {
        this.$router.push("/login");
      }
      this.$http.get("admin/querygood").then(res => {
        if (res.data.code == 200) {
          if(res.data.data.length==0){
            this.goodshow=false
          }else{
            this.goodshow=true
          }
          this.items = res.data.data;
          // console.log(this.items);
          // let str1=this.items[2].image.slice(2)
          // let str2=str1.substr(0, str1.length - 1)
          // console.log(str2,222)
          for (let index in this.items) {
            this.items[index].image = this.items[index].image.slice(2);
            this.items[index].image = this.items[index].image.substr(
              0,
              this.items[index].image.length - 1
            );
            this.items[index].image =
              "data:image/png;base64," + this.items[index].image;
          }
        }
      });
    },
    fench1() {
      this.$http.get("admin/querytag").then(res => {
        if (res.data.code == 200) {
          this.tagitems = res.data.data;
        }
      });
    },
    move(index) {
      this.items.splice(index, 1);
    },
    onConfirm(value) {
      this.value = value;
      this.showPicker = false;
    },
    tobuy(index) {
      //  console.log(this.items[index], "article");
      //   this.$router.push({
      //     name: "GoodBuy",
      //     params: { pk_refinfo: this.items[index], value: "test1" },
      //   });

      this.show = true;
      this.user.name = this.user2.name;
      this.$http.post("user/querycard", this.user).then(res => {
        if (res.data.code == 200) {
          //   console.log(res.data.data);
          this.na = res.data.data.map(function(v) {
            return v.card_id;
          });
          this.columns = this.na;
        }
      });

      this.good.name = this.items[index].name;
      this.good.price = this.items[index].price;

      this.good.user_name = this.user2.name;
    },
    beforeClose(action, done) {
      //   if(!this.userName || !this.userPass) {
      //      this.$toast("请输入用户名和密码")
      //      done(false) //不关闭弹框
      //   }
      if (action === "confirm") {
        //   setTimeout(done, )
        this.good.scard = this.value.toString();
        this.$http
          .post("/user/buygood", this.good)
          .then(res => {
            // console.log(res.data);
            if (res.data.code == 200) {
              this.$toast({ message: res.data.msg, icon: "success" });
              // done();
              done() //不关闭弹框
              this.value = "";
              this.good = {};
            } else {
              done(false) //不关闭弹框
              this.$toast({ message: res.data.msg, icon: "cross" });
            }
          })
          .catch(res => {
            done(false) //不关闭弹框
            this.$toast({ message: res.data.msg, icon: "cross" });
          });
      } else if (action === "cancel") {
        // console.log(999)
        done();
        this.value = "";
        this.good = {};
      }
    }
  }
};
</script>
<style>
/* .good1 {
  transition:width 2s;
}
  .good1:hover{
    width: 300px;
  } */
</style>
