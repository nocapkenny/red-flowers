<script setup>
import Header from "../../components/Header/Header.vue";
import { usePlantsStore } from "@/stores/plantsStore";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import Loader from "../../components/Loader/Loader.vue";
import Table from "@/components/Table/Table.vue";
const plantsStore = usePlantsStore();
const $route = useRoute();

onMounted(async () => {
  try{
    await plantsStore.getPlantById($route.params.id)
  }catch(e){
    console.log(e)
  }
})
</script>

<template>
  <Header />
  <div class="plant">
    <div class="plant__inner">
      <Loader v-if="plantsStore.isPlantLoading"/>
      <div class="plant__box" v-if="!plantsStore.isPlantLoading">
        <img
          :src="plantsStore.plant.img"
          alt=""
          class="plant__img"
          v-if="plantsStore.plant.img"
        />
        <img
          src="../../assets/images/sample.png"
          class="plant__img--sample"
          alt="cardImg"
          v-else
        />
        <div class="plant__info">
          <h5 class="plant__title title">
            {{ plantsStore.plant.species.name }}
          </h5>
          <p class="plant__text">
            {{ plantsStore.plant.species.description }}
          </p>
          <Table :head="['Высота', 'Контейнер', 'Цена']" :body="plantsStore.plant.goods_set"/>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
@use "../../assets/sytles/_vars" as *;
.plant {
  @include bg-section("../../assets/images/catalog-bg.jpg");
  justify-content: center;
  padding-left: 10px;
  padding-right: 10px;
  &__inner{
    @include content-box();
    padding: 0;
  }
  &__box {

    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    flex-wrap: wrap;
    @media (min-width: 600px) {
      flex-wrap: nowrap;
    }
  }
  &__info {
    margin-right: 30px;
  }
  &__img {
    max-width: 40%;
    height: 100%;
    border-radius: none;
    margin-right: 0;
    margin-top: 10px;
    @media (min-width: 600px) {
      border-top-left-radius: 15px;
      border-bottom-left-radius: 15px;
      margin-top: 0;
      margin-right: 10px;
    }
  }
  &__img--sample {
    margin-right: 0;
    @media (min-width: 600px) {
      margin-right: 10px;
    }
  }
  &__title {
    margin-top: 30px;
  }
  &__text {
    text-align: center;
    font-size: 18px;
  }
}
</style>
