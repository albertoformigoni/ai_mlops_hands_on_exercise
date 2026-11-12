# Task 2 report: Interactive app deployment

| Field | Value |
| --- | --- |
| Student | Alberto Formigoni |
| Dataset | bank_marketing.zip |
| Task | 2 |
| How to run | Clone the repository and navigate to its root directory. Run docker compose up --build -d, then open http://localhost:8501. Stop with docker compose down. Requires Docker Engine and Docker Compose. |
| Timebox | finished at 12:30 |

## 1. Summary
The second task is abput creating an interactive dashboard starting from the prvious exploratory analysis of the dataset.

I chose Streamlit to create a minimal dashboard able to display the basic statistics of the entire dataset or focusing on a single job among all customers. So selecting "All" in the job selection, you can see the toal number of customers and the subscription rate (both visual and numerical). Then, you can also see distribution of the customer age.
Furthermore, if you select a specific job, the dashboard shows the previous statistics regarding only the customers having that job.  

The second step of this task focused on containerizing the Streamlit application using Docker.\
I created the Dockerfile based on Python 3.12, using uv.lock to install the required dependencies. The container includes the application source code, the Bank Marketing dataset, and the Streamlit theme configuration. Unnecessary files, such as Jupyter notebooks, reports, ecc, are excluded using .dockerignore.\
Finally, I used Docker Compose to build and run the application, exposing port 8501 to access the dashboard through a web browser.

## 2. Approach and key decisions

I chose a single-page Streamlit app instead of a separate frontend and API, to keep the implementation simple considering the availble time. I reused the two Seaborn charts from the EDA notebook, added a job filter and two summary metrics, and kept the Dark Minimal interface theme.


## 3. Use of AI assistants

| Time | Purpose | What I kept or applied |
| --- | --- | --- |
| 11:13 | Help with customer counting in the job-selection visualization in Streamlit | filtered customer count and metrics. |
| 11:15 | Problem with the subscription-rate progress bar | Used `st.progress()` with the percentage converted to a value between 0 and 1. |
| 11:34 | How to split the dashboard into two columns | Used `st.columns(2)` for the EDA charts. |
| 11:38 | Fixing the width of the chart columns | Used Streamlit's wide-page layout.|
| 11:56 | Completing `.dockerignore` exclusions | |
