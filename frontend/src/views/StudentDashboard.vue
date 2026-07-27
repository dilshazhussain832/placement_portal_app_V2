<template>
  <div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

      <h2>Student Dashboard</h2>

      <button
        class="btn btn-danger"
        @click="logout"
      >
        Logout
      </button>

    </div>

    <div class="card shadow p-4 mb-4">

      <h4 class="mb-3">My Profile</h4>

      <div class="row">

        <div class="col-md-6 mb-3">
          <label class="form-label">Full Name</label>
          <input
            v-model="profile.full_name"
            class="form-control"
          >
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label">Phone</label>
          <input
            v-model="profile.phone"
            class="form-control"
          >
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label">Branch</label>
          <input
            v-model="profile.branch"
            class="form-control"
          >
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label">CGPA</label>
          <input
            v-model="profile.cgpa"
            class="form-control"
            type="number"
          >
        </div>

        <div class="col-md-6 mb-3">
          <label class="form-label">Passing Year</label>
          <input
            v-model="profile.passing_year"
            class="form-control"
            type="number"
          >
        </div>

        <div class="col-12 mb-3">
          <label class="form-label">Skills</label>
          <textarea
            v-model="profile.skills"
            class="form-control"
            rows="3"
          ></textarea>
        </div>

      </div>

      
      <div v-if="!resumeName || showUpload">

        <div class="col-12 mb-3">

          <label class="form-label">Resume (PDF)</label>

          <input
            type="file"
            class="form-control"
            accept=".pdf"
            @change="selectResume"
          >

        </div>

        <div class="mb-3">

          <button
            class="btn btn-success"
            @click="uploadResume"
          >
            Upload Resume
          </button>

        </div>

      </div>

      <div
        v-else
        class="alert alert-success d-flex justify-content-between align-items-center"
      >

        <div>

          <strong>Resume Uploaded:</strong>
          {{ resumeName }}

        </div>

        <div>

          <button
            class="btn btn-outline-primary btn-sm me-2"
            @click="viewResume"
          >
            View Resume
          </button>

          <button
            class="btn btn-warning btn-sm"
            @click="showUpload = true"
          >
            Replace Resume
          </button>

        </div>

      </div>

      <button
        class="btn btn-primary"
        @click="updateProfile"
      >
        Update Profile
      </button>

    </div>

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

          <tr v-if="drives.length === 0">
            <td colspan="100" class="text-center text-muted py-4">
              No placement drives are available at the moment.
            </td>
          </tr>

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
                v-if="!hasApplied(drive.id)"
                class="btn btn-primary btn-sm"
                @click="applyForDrive(drive.id)"
              >
                Apply
              </button>

              <button
                v-else
                class="btn btn-success btn-sm"
                disabled
              >
                Applied
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

    <div class="card shadow mt-4 p-4">

      <h4 class="mb-3">
        My Applications
      </h4>

      <table class="table table-bordered table-hover">

        <thead>
          <tr>
            <th>Company</th>
            <th>Job Title</th>
            <th>Applied On</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          <tr v-if="applications.length === 0">
            <td colspan="100" class="text-center text-muted py-4">
              You have not applied to any placement drives yet.
            </td>
          </tr>

          <tr
            v-for="application in applications"
            :key="application.application_id"
          >

            <td>{{ application.company_name }}</td>
            <td>{{ application.job_title }}</td>
            <td>{{ application.application_date }}</td>

            <td>

              <span
                v-if="application.status === 'Applied'"
                class="badge bg-primary"
              >
                Applied
              </span>

              <span
                v-else-if="application.status === 'Shortlisted'"
                class="badge bg-success"
              >
                Shortlisted
              </span>

              <span
                v-else-if="application.status === 'Rejected'"
                class="badge bg-danger"
              >
                Rejected
              </span>

              <span
                v-else
                class="badge bg-secondary"
              >
                {{ application.status }}
              </span>

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
import { useRouter } from "vue-router";
import { reactive } from "vue";

const router = useRouter();
const drives = ref([]);
const applications = ref([]);
const resumeFile = ref(null);
const resumeName = ref("");
const showUpload = ref(false);
const profile = reactive({
  full_name: "",
  phone: "",
  branch: "",
  cgpa: "",
  passing_year: "",
  skills: ""
});

const loadDrives = async () => {
  try {
    const response = await api.get("/student/drives");
    drives.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const loadApplications = async () => {
  try {
    const response = await api.get("/student/applications");
    applications.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

const applyForDrive = async (driveId) => {
  try {
    const response = await api.post(`/student/apply/${driveId}`);

    alert(response.data.message);

    await loadDrives();
    await loadApplications();

  } catch (error) {
    alert(
      error.response?.data?.message ||
      "Failed to apply."
    );
  }
};

const hasApplied = (driveId) => {
  return applications.value.some(
    application => application.drive_id === driveId
  );
};

async function logout() {

  try {

    const response = await api.post("/logout");

    alert(response.data.message);

    router.push("/");

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Logout failed."
    );

  }

}

async function loadProfile() {

  try {

    const response = await api.get("/student/profile");

    Object.assign(profile, response.data);
    resumeName.value = response.data.resume || "";

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Failed to load profile."
    );

  }

}

async function updateProfile() {

  try {

    const response = await api.put(
      "/student/profile",
      profile
    );

    alert(response.data.message);

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Profile update failed."
    );

  }

}

function selectResume(event) {

  resumeFile.value = event.target.files[0];

}

async function uploadResume() {

  if (!resumeFile.value) {

    alert("Please select a resume.");

    return;

  }

  const formData = new FormData();

  formData.append("resume", resumeFile.value);

  try {

    const response = await api.post(
      "/student/upload-resume",
      formData
    );

    resumeName.value = response.data.resume;
    resumeFile.value = null;
    showUpload.value = false;
    await loadProfile();

    alert(response.data.message);

  } catch (error) {

    alert(
      error.response?.data?.message ||
      "Resume upload failed."
    );

  }

}

function viewResume() {

  window.open(
    "http://localhost:5000/api/student/resume",
    "_blank"
  );

}

onMounted(() => {
  loadDrives();
  loadApplications();
  loadProfile();
});
</script>