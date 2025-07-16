import "react"
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react"
import { Outlet, Link, Navigate } from "react-router-dom";

export function Layout() {
    return <div className ="app-layout">
        <header>
            <div>
                <h1>
                    <nav>
                        <SignedIn>
                            <Link to="/">Home</Link>
                            <Link to="/history">History</Link>
                            <UserButton />
                        </SignedIn>
                    </nav>
                </h1>
            </div>
        </header>
        
    </div>
}

