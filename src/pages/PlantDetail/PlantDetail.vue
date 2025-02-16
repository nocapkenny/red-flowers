<script setup>
import Header from "../../components/Header/Header.vue";
import { usePlantsStore } from "@/stores/plantsStore";
const plantsStore = usePlantsStore();
</script>

<template>
  <Header />
  <div class="plant">
    <div class="plant__box">
      <h5 class="plant__title title">{{ plantsStore.plant.species.name }}</h5>
      <p class="plant__text">
        {{ plantsStore.plant.species.description }}
      </p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
.plant {
  @include bg-section("../../assets/images/catalog-bg.jpg");
  justify-content: center;
  padding-left: 10px;
  padding-right: 10px;
  &__box {
    @include content-box();
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
