import React, {useRef, useEffect, useState} from 'react'
import "./modelStreaming.css"

export function ModelStreaming() {
	const videoRef = useRef(null);
	const photoRef = useRef(null);

	const [hasPhoto, setHasPhoto]  = useState(false);

	const getVideo = () =>{
		navigator.mediaDevices.
			getUserMedia(
				{video: {width: 1920, height: 1080}})
			.then(stream => {
				let video = videoRef.current;
				video.srcObject = stream;
				video.play();
			})
			.catch(err =>{
				console.error(err)
			})
	}

	useEffect(() => {
		getVideo();
	}, [videoRef])

  	return (
    	<div className = "stream-model">
        	<div className='camera'>
           	 	<video ref={videoRef}></video>
           		<button className= 'snap-btn'> SNAP!</button>
        	</div>
			<div className = {"result" + (hasPhoto ? "hasPhoto" : "")}>
				<canvas ref = {photoRef}></canvas>
				<button className = 'close-btn'>CLOSE</button>
			</div>

    	</div>
  	)
}

