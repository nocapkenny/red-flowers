<script setup>

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  salary: {
    type: String,
    required: true
  },
  schedule: {
    type: String,
    required: true
  },
  experience: {
    type: String,
    required: true
  },
  education: {
    type: String,
    required: true
  },
  contactsPhone: {
    type: String,
    required: true
  },
  contactsEmail: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="vacancy">
    <h4 class="vacancy__title">{{ title }}</h4>
    <p class="vacancy__text">Условия</p>
    <ul class="vacancy__list">
      <li class="vacancy__list-item"><span>Зарплата: </span>{{ salary }}</li>
      <li class="vacancy__list-item">
        <span>График: </span>{{ schedule }}
      </li>
    </ul>
    <p class="vacancy__text">Требования</p>
    <ul class="vacancy__list">
      <li class="vacancy__list-item"><span>Образование: </span>{{ education }}</li>
      <li class="vacancy__list-item"><span>Опыт: </span>{{ experience }}</li>
    </ul>
    <p class="vacancy__text">Контакты</p>
    <ul class="vacancy__list">
      <li class="vacancy__list-item">
        <a href="tel:89999999999" class="vacancy__list-phone">{{ contactsPhone }}</a>
      </li>
      <li class="vacancy__list-item">
        <a href="mailto:mail@mail.com" class="vacancy__list-mail"
          >{{ contactsEmail }}</a
        >
      </li>
    </ul>
  </div>
</template>

<style src="./Vacancy.scss" scoped />
