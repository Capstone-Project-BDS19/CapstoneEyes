import React from "react"
import "./Portfolio.css"

export function Portfolio() {
    return (
  
      <section id = "portfolio">
          <br></br><br></br>
          <br></br><br></br>

  
          <div class = "portfolio container">
              <div><h1 class="section-title">Software Features</h1></div>

              <div class="feature-text">
                  <br></br><br></br>
              <p>Enjoy a range of features that our Eye Strain and Drowsiness Detection system has to offer.</p>
              </div>
             
              <br></br>
             
              <div class="portfolio-items">
                  <div class="portfolio-item">
                      <div class="icon"><img src="/images/real.png"/></div>
                      <div class="portfolio-info">
                          <h2>Real Time Detection</h2>
                          <p><b>Track eye movements live as you work, drive or study</b></p>
                      </div>
                  </div>
              </div>
              <br></br>
              <div class="portfolio-items">
                  <div class="portfolio-item">
                      <div class="icon"><img src="/images/alert.png"/></div>
                      <div class="portfolio-info">
                          <h2>Alert System</h2>
                          <p><b>Be notified instantly if you feel drowsy or have eye strain</b></p>
                      </div>
                  </div>
              </div>
              <br></br>
              <div class="portfolio-items">
                  <div class="portfolio-item">
                      <div class="icon"><img src="/images/report.png"/></div>
                      <div class="portfolio-info">
                          <h2>Generate Report</h2>
                          <p><b>Track your eye health over time and monitor your progress </b></p>
                      </div>
                  </div>
                  <br></br><br></br>
              </div>
          </div>
      </section>
      
      
      
      
      
      
    )
  }