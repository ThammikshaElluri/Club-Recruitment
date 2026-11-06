# Team 12 · Club Recruitment

| Team | Partner 1 |
|---|---|---|---|---|
| [] | [Thammiksah] | None | Club Recruitment | 

## 1. Who is doing what

| Day | Partner | What will you do? | Completed? | What are you going to work on next? | Stuck on? |
|---|---|---|---|---|---|
| Day 1 | Thammiksha | Build the backend, database, and three main endpoints |  ✅ | checking swagger is working | No |


## 2. Endpoint tracker

Use the exact method and paths from your PRD. Status: ✅ done · 🟡 in progress · ⬜ not started

| # | Method + path | Built | Rules checked in /docs | Connected to React | Who |
|---|---|---|---|---|---|
| E1 | GET /clubs | ✅ | ✅ | ✅ | Thammiksha |
| E2 | POST /clubs | ✅ |✅  | ✅ | Thammiksha |
| E3 |GET /clubs/{club_id} | ✅ |✅  | ✅ | Thammiksha |
| E4 | PATCH /clubs/{club_id}/recruitment | ✅ | ✅ | ✅ | Thammiksha |
| E5 | POST /clubs/{club_id}/applications |  | ✅ | ✅ | Thammiksha |
| E6 | PATCH /applications/{application_id}/status | ✅ | ✅ | ✅ | Thammiksha |


| # | What it does | Method | Path | Request body | Success code | Error codes |
|---|---|---|---|---|---|---|
| E1 | Get all clubs; optionally filter by category. Each includes its count of applications that aren’t withdrawn. | GET | /clubs?category={category} | None | 200| 400 invalid category |
| E2 | Get one club by ID, with its applications. | GET | /clubs/{club_id} | None | 200 | 404 club not found |
| E3 | Add a club. It starts recruiting. | POST | /clubs | {"name":"…","category":"…","seats":10,"deadline":"YYYY-MM-DD"}| 201 | 400 invalid input |
| E4 | Open or close a club’s recruitment. | PATCH | /clubs/{club_id}/recruitment | {"is_open":true} | 200 | 404club not found; 400 invalid input |
| E5 | Apply to a club. The application starts as applied. | POST | /clubs/{club_id}/applications` | {"roll_number":"…","reason":"…"} | 201 | 404 club not found; 400 invalid input; 409 recruitment closed or duplicate application |
| E6 | Move an application to shortlisted, selected, or rejected. | PATCH`| /applications/{application_id}/status | {"status":"shortlisted"} | 200 | 404 application not found; 400 invalid status or transition |

