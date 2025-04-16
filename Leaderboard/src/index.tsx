import React, { useState, useEffect } from 'react';
import ReactDOM from "react-dom"
import Leaderboard from "./LeaderboardComp"

import "./index.css"

import mockDataGen from "./mocks/performances_generation.json"
import mockDataRep from "./mocks/performances_repair.json"
import mockDataTest from "./mocks/performances_testgen.json"
import mockDataExec from "./mocks/performances_execution.json"


const LeaderboardTabs = () => {
  // State to track the currently selected tab
  const [activeTab, setActiveTab] = useState('tab1');
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  // Function to render the leaderboard based on the selected tab
  const renderLeaderboard = () => {
    // console.log(activeTab);
    switch (activeTab) {
      case 'tab1':
        return <Leaderboard theme={{ base: "light" }} args={mockDataGen} />;
      case 'tab2':
        return <Leaderboard theme={{ base: "light" }} args={mockDataRep} />;
      case 'tab3':
        return <Leaderboard theme={{ base: "light" }} args={mockDataTest} />;
      case 'tab4':
        return <Leaderboard theme={{ base: "light" }} args={mockDataExec} />;
      default:
        return <div>Select a tab</div>;
    }
  };
  return (
    <div className="tabs-container">
      <ul className={`tabs ${isMobile ? 'mobile' : ''}`}>
        <li className={activeTab === 'tab1' ? 'is-active' : ''} onClick={() => setActiveTab('tab1')}><a>Code Generation</a></li>
        <li className={activeTab === 'tab2' ? 'is-active' : ''} onClick={() => setActiveTab('tab2')}><a>Self Repair</a></li>
        <li className={activeTab === 'tab3' ? 'is-active' : ''} onClick={() => setActiveTab('tab3')}><a>Test Output Prediction</a></li>
        <li className={activeTab === 'tab4' ? 'is-active' : ''} onClick={() => setActiveTab('tab4')}><a>Code Execution</a></li>
      </ul>
      <div className="tab-content">
        {renderLeaderboard()}
      </div>
    </div>
  );
};


ReactDOM.render(
  <React.StrictMode>
    <section className="hero">
      <div className="hero-body">
        <div className="container is-max-desktop">
          <div className="columns is-centered">
            <div className="column has-text-centered">
              <h1 className="title is-1 publication-title">
                LiveCodeBench: Holistic and Contamination Free Evaluation of
                Large Language Models for Code
              </h1>
              <div className="column has-text-centered">
                <div className="publication-links">
                  <span className="link-block">
                    <a href="https://arxiv.org/abs/2403.07974"
                      className="external-link button is-normal is-rounded is-dark">
                      <span className="icon">
                        <i className="fas fa-file-pdf"></i>
                      </span>
                      <span>Paper</span>
                    </a>
                  </span>

                  <span className="link-block">
                    <a href="https://github.com/LiveCodeBench/LiveCodeBench"
                      className="external-link button is-normal is-rounded is-dark">
                      <span className="icon">
                        <i className="fab fa-github"></i>
                      </span>
                      <span>Code</span>
                    </a>
                  </span>

                  <span className="link-block">
                    <a href="https://huggingface.co/livecodebench/"
                      className="external-link button is-normal is-rounded is-dark">
                      <span className="icon">
                        <i className="far fa-images"></i>
                      </span>
                      <span>Data</span>
                    </a>
                  </span>

                  <span className="link-block">
                    <a
                      href="https://livecodebench.github.io/"
                      className="external-link button is-normal is-rounded is-dark"
                    >
                      <span className="icon">
                        <i className="fas fa-home"></i>
                      </span>
                      <span>Home</span>
                    </a>
                  </span>

                </div>
              </div>
              <div className="column has-text-centered">
                <LeaderboardTabs />
              </div>


              <section className="section">
                <div className="container is-max-desktop">
                  <div className="columns is-centered has-text-centered">
                    <div className="column is-four-fifths">
                      <h2 className="title is-3">Submitting Custom Models</h2>
                      <div className="content has-text-justified">
                        <p>
                          To submit models you can create a pull request on our <a
                            href="https://github.com/LiveCodeBench/submissions">Github</a>. Particularly, you can copy your model
                          generations folder from `output` to the `submissions` folder and create a pull request. We will review the
                          submission and add the model to the leaderboard accordingly.

                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </section>



            </div>
          </div>
        </div>
      </div>
    </section>
  </React.StrictMode>,
  document.getElementById("root")
)