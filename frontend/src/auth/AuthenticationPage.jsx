import "react"
import {SignIn, SignUp, SignedIn, SignedOut} from '@clerk/clerk-react'

export function AuthenticationPage() {
    return <div className="auth-container">
        <SignedIn>

            <div className="redirect-message"> 
                <p>Welcome to the application!</p>
            </div>

        </SignedIn>

        <SignedOut>
            <SignIn routing="path" path="/sign-in" />
            <SignUp routing="path" path="/sign-up" />
        </SignedOut>

    </div>
}

