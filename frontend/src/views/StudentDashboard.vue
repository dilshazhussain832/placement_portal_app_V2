<template>
  <div class="container mt-5">

    <h2 class="mb-4">
      Student Dashboard
    </h2>

    <div class="card shadow p-4">

      <h4 class="mb-3">
        Available Placement Drives
      </h4>

      <table class="table table-bordered table-hover">

        <thead>

          <tr>
            <th>Company</th>
            <th>Job Title</th>
            <th>Eligibility</th>
            <th>Salary</th>
            <th>Deadline</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="drive in drives"
            :key="drive.id"
          >

            <td>{{ drive.company_name }}</td>
            <td>{{ drive.job_title }}</td>
            <td>{{ drive.eligibility }}</td>
            <td>{{ drive.salary }}</td>
            <td>{{ drive.application_deadline }}</td>

            <td>

              <button
                class="btn btn-primary btn-sm"
                @click="applyForDrive(drive.id)"
              >
                Apply
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const drives = ref([]);

const loadDrives = async () => {
  try {
    const response = await api.get("/student/drives");
    drives.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const applyForDrive = async (driveId) => {
  try {
    const response = await api.post(`/student/apply/${driveId}`);

    alert(response.data.message);

    await loadDrives();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to apply."
    );
  }
};

onMounted(() => {
  loadDrives();
});
</script>