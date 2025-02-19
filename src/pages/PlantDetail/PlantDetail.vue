<script setup>
import Header from "../../components/Header/Header.vue";
import { usePlantsStore } from "@/stores/plantsStore";
const plantsStore = usePlantsStore();
</script>

<template>
  <Header />
  <div class="plant">
    <div class="plant__box">
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
        <h5 class="plant__title title">{{ plantsStore.plant.species.name }}</h5>
        <p class="plant__text">
          {{ plantsStore.plant.species.description }}
        </p>
        <table class="plant__table">
          <thead>
            <tr>
              <th>Высота</th>
              <th>Контейнер</th>
              <th>Цена</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in plantsStore.plant.goods_set">
              <td>{{ item.height }}</td>
              <td>{{ item.pot_size }}</td>
              <td>{{ item.price }}</td>
            </tr>
          </tbody>
        </table>
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
  &__box {
    @include content-box();
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
    padding: 0;
    margin-bottom: 20px;
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
  &__img--sample{
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
  &__table {
    width: 80%;
    margin: 0 auto;
    border-collapse: collapse;
    margin-bottom: 30px;
    th,
    td {
      border: 1px solid $black;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: $red;
      color: $white;
    }
  }
}
</style>
