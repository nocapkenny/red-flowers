<script setup>
import { onMounted, ref } from "vue";
import { Plant } from "../../../backend/src/api.js";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";
import axios from "axios";


const test = async () => {
  try {
    const res = await Plant.objects.filter({})
    console.log(res)
  } catch (error) {
    console.log(error);
  }
}

const isBigCard = ref(false);

onMounted(() => {
  test()
})
</script>

<template>
  <Header />
  <div class="catalog">
    <Filters v-model:isBigCard="isBigCard" />
    <CardList :isBigCard="isBigCard" />
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
.catalog {
  @include bg-section("../../assets/images/catalog-bg.jpg");
}
</style>
