# Join Assistant Setup
This is really easy to setup, all you need is this program and your ROBLOSECURITY cookie.
If you want information on how your ROBLOSECURITY cookie is used, please check the privacy policy.

1. Copy your .ROBLOSECURITY cookie from the Developer console on the ROBLOX website
2. Open the program, and type configure.cookie
3. Follow the prompts and paste in your cookie.
4. You're all done!

If you want more information on the various settings, check the settings catagory. 

<hr>

# Commands
These are commands you can run in the appliction
### new-event 
> Args: `duration`, `starttime` <br><br>
> This command will setup a new event with the provided arguments. If none are provided, it will prompt. This returns a custom event id
### list-events 
> No arguments<br><br>
> Lists all of the events currently saved and their IDs
### end-event 
> Args: `event id`<br><br>
> This event will end an event early which matches the provided id. If no ID is provided it uses the most recent ID
### extend-event 
> Args: `event id`, `duration`<br><br>
> Adds the duration in minutes to the event with the corresponding id. If you do not provide an ID it will fallback to the most recent ID. If you do not provide a duration, it will prompt you
### edit-cookie
> No arguments <br><br>
> This will configure the ROBLOSECURITY cookie the application uses.
<hr>

# Cookies
Because this application needs to interact with your ROBLOX account settings, you need a ROBLOSECURITY cookie. This is a token specific to your ROBOX account that resets when you log out and log in, or change your password. When you first start the program, you will need to configure your cookie with `edit-cookie`. Please paste the full cookie in, **Including the warning text**

# Privacy Policy
Because this application handles sensitive data pertaining to your ROBLOX account (your account's ROBLOSECURITY cookie), this body of text shows what we (the program) do with the data you enter.

The data you enter into this program is protected in a `.env` file within your device. This is a way of safely storing your data.
Your data is never transmitted, broadcasted or otherwise sent to any external server or removed from your device, and is only used in sending requests to ROBLOX owned servers. This part is essential to toggle your join settings on ROBLOX.

If you want more information about `.env` files, please check [dotenv.org](https://www.dotenv.org/docs/security/env)'s website