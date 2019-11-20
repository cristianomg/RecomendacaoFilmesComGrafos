import React from 'react';
import Loader from 'react-loader-spinner';
import { usePromiseTracker } from "react-promise-tracker";


const LoadingIndicator = props => {
    const { promiseInProgress} = usePromiseTracker();
    return (
        promiseInProgress &&
        <div
            style={{
               margin: "20px",
               width: "100%",
               height: "100",
               display: "flex",
               justifyContent: "center",
               alignItems: "center",
               flexDirection: "column-reverse"
            }}
        >
        <strong style={{
            fontSize: "15px",
            color: "#ff002b",
        }}>Carregando</strong>
        <Loader type="ThreeDots" color="#ff002b" height="100" width="100" />     
      
    </div>
    );
}

export default LoadingIndicator;