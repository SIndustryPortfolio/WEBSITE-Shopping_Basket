var PageModule = {}

// Functions
// MECHANICS
async function Initialise() 
{
    // CORE
    let CoreConfig = window.Config;
    let {default: CurrentPageModule} = await import(CoreConfig["StaticPath"] + "JS/" + CoreConfig["CurrentPageName"] + ".js"); // Explicitly define default export

    // Elements
    // DIVS
    let SplashScreenLoaderDiv = document.getElementById("SplashScreenLoader");

    // Functions
    // MECHANICS
    function RemoveSplashScreen() 
    {
        // Functions
        // INIT
        SplashScreenLoaderDiv.classList.add("SplashScreenLoader-Hidden");

        SplashScreenLoaderDiv.addEventListener("transitionend", () => { // CLEAN UP
            SplashScreenLoaderDiv.parentNode.removeChild(SplashScreenLoaderDiv);
        });
    }

    function Loaded() 
    {
        // Functions
        // INIT

        if (SplashScreenLoaderDiv != undefined) 
        {
            setTimeout(RemoveSplashScreen, 500);
        }
        
        return CurrentPageModule.Initialise();
    }

    // DIRECT
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", Loaded);
    }
    else 
    {
        Loaded();
    }

    window.addEventListener("beforeunload", () => {
        // Functions
        // INIT
        return CurrentPageModule.End();
    });
}

// DIRECT
PageModule.Initialise = Initialise;

export default PageModule;