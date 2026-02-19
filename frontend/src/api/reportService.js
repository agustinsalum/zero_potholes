import axiosInstance from "./axiosInstance";

export const createPublicReport = async (reportData) => {
  const response = await axiosInstance.post(
    "reports/public-create/",
    reportData
  );
  return response.data;
};

export const getApprovedReports = async () => {
  const response = await axiosInstance.get("reports/approved/");
  return response.data;
};
