import React, {useState} from 'react'; //rfce
import {Link} from 'react-router-dom';
import * as FaIcons from "react-icons/fa"
import * as AiIcons from "react-icons/ai"
import { SidebarData } from './SideBarData';
import "./NavBar.css"
import { IconContext } from 'react-icons';

export function NavBar() {
    const [sidebar, setSidebar] = useState(false);

    const showSidebar = () => {
        setSidebar(!sidebar);
    }

    return (
        <div className = "navbar-wrapper">
        <IconContext.Provider value = {{color: '#fff'}}>
                <div className = "navbar">
                    <Link to ="#" className = 'menu-bars'>
                        <FaIcons.FaBars onClick = {showSidebar}/>
                    </Link>
                    <div className = "project-name">
                        <span className = "prj-title"> Eye's strain and drowsiness detection</span>
                    </div>
                    <div className = "login-signup">
                        <Link to ="/login" className = "login"> Login </Link>
                        <Link to ="/signup" className = "signup"> Signup</Link>
                    </div>
                </div>
                <nav className = {sidebar ? 'nav-menu active' : 'nav-menu'}>
                    <ul className = "nav-menu-items" onClick={showSidebar}>
                        <li className = "navbar-toggle">
                            <Link to = "#" className = "menu-bars">
                                <AiIcons.AiOutlineClose /> 
                            </Link>
                        </li>
                        {SidebarData.map((item, index) => {
                            return (
                                <li key = {index} className= {item.cName}>
                                    <Link to ={item.path}> 
                                    {item.icon}
                                    <span> {item.title} </span>
                                    </Link>
                                </li>
                            )
                        })}
                    </ul>
                </nav>
            </IconContext.Provider>
        </div>
  )
}
