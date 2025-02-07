**Deploying Number Classification API Using AWS Lambda.**

**Introduction**

Numbers aren't just digits; they have personality! This AWS Lambda-powered API analyzes any given number, uncovering its mathematical essence. 
It determines whether the number is prime (a lone wolf), perfect (mathematically flawless), or an Armstrong number (showing off its power digits). 
Additionally, it computes the digit sum and classifies the number as odd or even. For an extra touch of geeky fun, the API fetches a fascinating mathematical fact from the Numbers API - because every number has a story to tell.
Seamlessly scalable and built for efficiency, this API brings number crunching to a whole new level.

**Feature:**

**Input Validation:** No nonsense allowed! Ensures the input is a valid integer before diving into the math.

**Mathematical Analysis:** Because numbers deserve a full diagnostic report.

Deploying Number Classification API Using AWS Lambda. Is your number a solo act or part of the composite crowd?

**Perfect Number Check:** Finds out if your number is mathematically flawless.

**Armstrong Check:** Determines if your number is flexing its narcissistic muscles.
Digit Sum: Adds up the digits to reveal their collective wisdom.

 **Properties List:** A neat classification of your number's identity.
If it's an Armstrong number, it proudly returns its status along with its parity (odd/even), e.g., ["armstrong", "odd"].
Otherwise, it humbly reports just its parity, e.g., ["odd"] or ["even"].

**Fun Fact**: Numbers have stories too! Fetches an interesting mathematical fact via the Numbers API because learning should never be boring.

This API gracefully handles positive and negative numbers, ensuring even the grumpiest negatives get analyzed. Got a floating-point number? No problem! It gets smoothly converted to an integer before processing. Whether your number is whole, fractional, or just having an identity crisis, this API has it covered.
Required JSON Response Format (200 OK):


**{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}**


Required JSON Response Format (400 Bad Request)

**{
    "number": "alphabet",
    "error": true
}**


**Functionality**

Accepts GET requests with a number parameter.
Returns JSON in the specified format.
Accepts all valid integers as the only possible inputs
Provides appropriate HTTP status codes.

**Steps**

**1️. Create a GitHub Repo & Clone It** - Because every great project starts with git clone.

**2. Navigate into the Repo** - Get inside your new code home with cd <repo-name>.

**3️. Create a "package" Folder **- This is where your dependencies will live. Think of it as their VIP lounge.

**4️. Move into the "package" Folder & Install Dependencies** - Step inside (cd package) and install requests using
**pip install requests -t .**

**4️. Write Your Lambda Code** - Inside the "package" folder, create a file named lambda_function.py. This is where the magic happens-write your Python logic, save the file, and get ready to package your brilliance.

**5️. Bundle It Up** - Zip the entire folder like a pro using

**Compress-Archive -Path * -DestinationPath zippackage.zi**p

**6. Create Your Lambda Function**- Head to the AWS Management Console, navigate to Lambda, and create a new function.

**Don't forget to tweak the settings:**

Expand Additional Configuration
Enable Function URL (because your API deserves to be accessible)
 Configure Public Access & CORS so your API can talk to the world.

**7️. Upload, Deploy & Test**

Upload the ZIP package,
Deploy the function,
Run a test to make sure everything works like a charm.

 If it passes, you're ready for the next step!
 
**8️. Set Up API Gateway –**

Create an API Gateway and link it to your Lambda function.
Choose HTTP integration for seamless connectivity.
Once configured, invoke the API URL and watch your function come to life.

Boom! Your API is now live and ready to roll

**Key Takeaways**

Deploying an API using AWS Lambda Function URLs turned out to be a game-changer - efficient, cost-effective, and hassle-free. Here's what we learned along the way:

Perfect for Lightweight APIs - No infrastructure headaches! AWS Lambda makes it easy to deploy simple APIs without worrying about servers.

Streamlined Deployment - Function URLs cut out the middleman (API Gateway) when all you need is a basic public endpoint. Fewer moving parts = fewer headaches.

Error Handling Matters - Returning valid JSON responses isn't just polite; it makes debugging smoother and keeps your API friendly to clients.

CORS Configuration is Key - Forgetting to set up CORS properly? Say hello to frustrating request failures. Configuring it right ensures smooth interactions with web apps.

Fast, Easy, and Scalable - With Function URLs, you get a no-fuss, low-latency API that scales automatically - because efficiency should never be complicated.

Bottom line? AWS Lambda Function URLs make API deployment faster, cheaper, and simpler while keeping performance intact.

**Conclusion**

This project wasn't just about deploying an API - it was a deep dive into the real-world mechanics of AWS Lambda, FastAPI, and CORS configurations. Each challenge tackled brought new insights, making it a crucial milestone in my cloud journey.

As I continue leveling up in the HNG DevOps Internship, I'm eager to take on bigger, more complex deployments, optimize API performance, and refine my serverless skills.

Thinking about deploying a FastAPI service on AWS Lambda? Lambda Function URLs are a game-changer - simple, cost-effective, and perfect for lightweight APIs. Definitely worth trying!

On to the next adventure in the cloud!
