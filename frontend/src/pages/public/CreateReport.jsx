import { createReport } from "../api/reportService";

const handleSubmit = async (e) => {
  e.preventDefault();

  const report = {
    title: "Test Pothole",
    description: "Test description",
    latitude: -34.6037,
    longitude: -58.3816,
    severity: 2,
    city: 1
  };

  try {
    const data = await createReport(report);
    console.log("Report created:", data);
  } catch (error) {
    console.error("Error creating report:", error);
  }
};
