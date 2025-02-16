<script setup>
import { usePlantsStore } from "@/stores/plantsStore";
const plantsStore = usePlantsStore();

const props = defineProps({
  isBigCard: {
    type: Boolean,
    default: false,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  descr: {
    type: String,
    required: true,
  },
  sort: {
    type: String,
    required: true,
  },
  nameLatin: {
    type: String,
    required: true,
  },
  height: {
    type: String,
    required: true,
  },
  pot:{
    type: String,
    required: true
  },
  id: {
    type: Number,
    required: true
  },
});

</script>

<template>
  <div class="card">
    <img src="../../assets/images/1.jpg" class="card-img-top" alt="cardImg" />
    <div class="card-body d-flex flex-column justify-content-between">
      <h5 class="card-title">{{ name }}</h5>
      <p class="card-text">{{ sort ? sort : nameLatin }}</p>
      <div class="card__specs" v-if="isBigCard">
        <p class="card__spec"><span>Высота:</span> {{ height }} см</p>
        <p class="card__spec"><span>Горшок:</span> {{ pot }} см</p>
      </div>
      <router-link class="card__btn btn btn-primary" @click="plantsStore.getPlantById(id)" :to="/plant/ + id"
        >Узнать больше</router-link
      >
    </div>
  </div>
</template>

<style src="./Card.scss" scoped />
