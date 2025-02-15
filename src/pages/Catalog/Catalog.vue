<script setup>
<<<<<<< HEAD
import { ref } from "vue";
import Header from "../../components/Header/Header.vue";
import CardList from "../../components/CardList/CardList.vue";
import Filters from "../../components/Filters/Filters.vue";

const isBigCard = ref(false);
</script>

<template>
  <Header />
  <div class="catalog">
    <Filters v-model:isBigCard="isBigCard" />
    <CardList :isBigCard="isBigCard" />
  </div>
=======
import { ref } from 'vue'
import Header from '../../components/Header/Header.vue'
import CardList from '../../components/CardList/CardList.vue'
import Filters from '../../components/Filters/Filters.vue'

const isBigCard = ref(false)


</script>

<template>
    <Header/>
    <div class="catalog">
        <Filters v-model:isBigCard="isBigCard"/>
        <CardList :isBigCard="isBigCard"/>
    </div>
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
<<<<<<< HEAD
.catalog {
  @include bg-section("../../assets/images/catalog-bg.jpg");
}
</style>
=======
.catalog{
    @include bg-section("../../assets/images/catalog-bg.jpg");
}
</style>
>>>>>>> 8e0ab739f64b0bbd314ac9aa75f85d58fe4b629b
