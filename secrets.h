/*

          WIFI SETUP

*/

#define WIFI_SSID     "Garden"
#define WIFI_PASSWORD "6354207C7A"

/*

          FIREBASE SETUP

  ------------------------------------------------
  IMPORTANT: Choose Firebase Initialization Method
  ------------------------------------------------

  1. ** Test Mode (No Authentication) **:

     - Ensure Firebase rules are set to allow public access. Set the rules as follows:
       {
         "rules": {
           ".read": "true",
           ".write": "true"
         }
       }

  2. ** Locked Mode (With Authentication) **:

     - Obtain your Firebase Authentication Token:
       1. Open your Firebase Console: https://console.firebase.google.com/
       2. Navigate to your project.
       3. Click on the gear icon next to "Project Overview" and select "Project settings".
       4. Go to the "Service accounts" tab.
       5. In the "Database secrets" section, click on "Show" to reveal your authentication token.

     - Ensure Firebase rules require authentication. Set the rules as follows:
       {
         "rules": {
           ".read": "auth != null",
           ".write": "auth != null"
         }
       }

  Note: Using authentication is recommended for production environments to secure your data.
*/

/* Test Mode (No Authentication) */
#define REFERENCE_URL "https://home-garden-25b17.firebaseio.com/"

/* Uncomment the following line for Locked Mode (With Authentication) */
 #define AUTH_TOKEN "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c"
