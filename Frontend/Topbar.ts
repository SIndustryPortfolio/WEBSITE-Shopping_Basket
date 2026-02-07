var PageModule: {[key : string]: any} = {}

// Functions
// MECHANICS
async function Initialise() : Promise<void>
{
    // CORE
    let CoreConfig = window.Config;
    let {default: CurrentPageModule} = await import(CoreConfig["StaticPath"] + "JS/" + CoreConfig["CurrentPageName"] + ".js"); // Explicitly define default export

    // Elements
    // DIVS
    let SplashScreenLoaderDiv = document.getElementById("SplashScreenLoader") as HTMLDivElement;

    // Functions
    // MECHANICS
    function RemoveSplashScreen() : void
    {
        // Functions
        // INIT
        SplashScreenLoaderDiv.classList.add("SplashScreenLoader-Hidden");

        SplashScreenLoaderDiv.addEventListener("transitionend", () => { // CLEAN UP
            if (!SplashScreenLoaderDiv.parentNode) 
            {
                return;
            }

            SplashScreenLoaderDiv.parentNode.removeChild(SplashScreenLoaderDiv);
        });
    }

    function Loaded() : void
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