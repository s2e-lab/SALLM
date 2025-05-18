import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

class SomehowRequired extends StreamlitComponentBase {
  public render = (): ReactNode => {
    return <span></span>
  }
}

export default withStreamlitConnection(SomehowRequired)
