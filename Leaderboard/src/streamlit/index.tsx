import React from "react"
import ReactDOM from "react-dom"
import SomehowRequired from "./SomehowRequired"
import Leaderboard from "../LeaderboardComp"

ReactDOM.render(
  <React.StrictMode>
    <SomehowRequired />
    <Leaderboard />
  </React.StrictMode>,
  document.getElementById("root")
)
