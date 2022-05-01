import React, {useEffect, useState} from 'react';
import Posts from "./Apis/Posts"
import PostLoadingComponent from "./Apis/PostLoading"

function AppTest(){
    const PostLoading = PostLoadingComponent(Posts);
    const [appState, setAppState] = useState({
        loading: false,
        posts: null
    });
    useEffect(() => {
        setAppState({loading:true});
        const apiUrl = 'http://127.0.0.1:8000/api/';
        fetch(apiUrl)
            .then((data) => data.json())
            .then((posts) => {
                setAppState({loading: false, posts: posts})
            });
    }, [setAppState]);
    return(
        <div className='App'>
            <h1> Latest posts</h1>
            <PostLoading isLoading = {appState.loading}
                        posts = {appState.posts} />
        </div>
    )
}

export default AppTest;