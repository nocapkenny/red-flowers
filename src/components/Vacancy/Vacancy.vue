<template>
  <div class="vacancy">
    <h4 class="vacancy__title">Название вакансии</h4>
    <p class="vacancy__text">Условия</p>
    <ul class="vacancy__list">
      <li class="vacancy__list-item"><span>Зарплата: </span>Договорная</li>
      <li class="vacancy__list-item">
        <span>График: </span>Полный рабочий день
      </li>
    </ul>
    <p class="vacancy__text">Требования</p>
    <ul class="vacancy__list">
      <li class="vacancy__list-item"><span>Образование: </span>Высшее</li>
      <li class="vacancy__list-item"><span>Опыт: </span>1 год</li>
    </ul>
    <p class="vacancy__text">Контакты</p>
    <ul class="vacancy__list">
      <li class="vacancy__list-item">
        <a href="tel:79999999999" class="vacancy__list-phone">+7(999)999-99-99</a>
      </li>
      <li class="vacancy__list-item">
        <a href="mailto:mail@mail.com" class="vacancy__list-mail"
          >mail@mail.com</a
        >
      </li>
    </ul>
  </div>
</template>

<style src="./Vacancy.scss" scoped />
