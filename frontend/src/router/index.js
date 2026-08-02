import { createRouter, createWebHistory } from "vue-router";

import LoginView from "../views/LoginView.vue";
import AdminDashboard from "../views/AdminDashboard.vue";
import StudentDashboard from "../views/StudentDashboard.vue";
import CompanyDashboard from "../views/CompanyDashboard.vue";
import StudentRegister from "../views/StudentRegister.vue";
import CompanyRegister from "../views/CompanyRegister.vue";
import HomePage from "../views/HomePage.vue";

const routes = [
  {
  path: "/",
  redirect: "/home",
  },
  {
    path: "/login",
    component: LoginView,
  },
  {
    path: "/home",
    component: HomePage,
  },
  {
    path: "/student-register",
    component: StudentRegister,
  },
  {
      path: "/company-register",
      component: CompanyRegister,
  },
  {
    path: "/admin",
    component: AdminDashboard,
  },
  {
    path: "/student",
    component: StudentDashboard,
  },
  {
    path: "/company",
    component: CompanyDashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;