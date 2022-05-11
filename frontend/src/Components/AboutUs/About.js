import React from "react"
import "./About.css"

export function About(){
  return (
    <>
    <section id="about">
    <img src="/images/banner.jpg"></img>
      <div class="about container">

        <div className="col-right">
          <h1 className="section-title">ABOUT US</h1>
          <h2>We are Data Science Students</h2>
          <br></br>
          <p>Our team is from S P Jain School of Global Management in Sydney.
            We are Quan, Tram, Nhi and Swetlana.
            <br></br>
            The Eye Strain and Drowsiness 
            Detection system is our 2022 capstone project and our passion.
          </p>

          <p>With everything going online due to the pandemic, we realised that 
            people using the screen a lot would need a system that will alert them 
            if they start experiencing eye strain and drowsiness symptoms. We hope 
            you will appreciate using our software!</p>
        </div>
 
 
      </div>
    </section>

    </>
  )
}
