from click import Option
import streamlit as st
st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")

st.title("LiveFit ")
st.write("Enter the Details")
# with st.form("Details"):
st.write("Inside the form")
age = st.slider("Age")
   
gen = st.selectbox(
    'Gender:',
    ('Male', 'Female','Others'))
submitted = st.button("Submit")

if submitted:
    st.write("Age : ", age, "Gender", gen)
    if age in range(0,30) :
            st.title("Key Nutrients You Need Now ")
            st.write("""

            Protein: Protein helps keep you full and provides the building blocks so you can make and keep muscle. "Recent studies suggest that, at a minimum, we need 60 to 70 grams of protein a day," says Leslie Bonci, M.P.H., R.D., director of sports medicine at the University of Pittsburgh Medical Center. Get your quota by eating skinless white meat poultry, lean steak, fish, eggs, beans, tofu, and low-fat dairy. (Here's more on how much protein you really need per day.)

            Potassium: In order for your muscles and heart to function properly, you need to consume a hefty dose of potassium. But most women in the U.S. aged 20 to 39 get less than half the recommended amount, according to the USDA. Munching on 2 cups of fruit and 2 1/2 cups of veggies daily will help you get all the potassium you need.

            Omega-3 fatty acids: These polyunsaturated fatty acids may boost serotonin, a feel-good chemical in your brain that research shows may be linked to depression when transmitted in low levels. Since women are twice as likely as men to be diagnosed with depression, start incorporating salmon and tuna into your diet, which are rich in omega-3s. You can also get your fill from walnuts, ground flaxseed, and canola oil.""")

            st.title("The Age Diet Chart for Your 20s")

            st.write("""Load up your desk drawer or office fridge with these healthy treats.

Greek yogurt (6 ounces) with 1 tablespoon chopped walnuts
Reduced-fat string cheese and 10 whole-grain crackers
Granola bar and a nonfat latte
4 ounces nonfat cottage cheese and a mini box of raisins
6 dried apricots and 2 tablespoons sunflower seeds
Energy bar and 12 almonds
20 mini carrots dipped in 1/4 cup hummus
Single-serve vanilla soy milk and 1/2 cup whole-grain cereal
Your 20-Something Meal Plan

Breakfast: 24-ounce Jamba Juice Protein Berry Pizzazz Smoothie. It's packed with protein to keep you satisfied. (Or whip up one of these healthy smoothies at home.)

Morning Snack: 1 packet instant oatmeal sprinkled with 1 tablespoon ground flaxseed

Lunch: Asian grilled-chicken salad with mixed greens, edamame, mandarin oranges, tomatoes, and low-fat vinaigrette

Afternoon Snack: Medium orange and 1 tablespoon chopped walnuts

Dinner: 7 pieces sushi and 1 cup edamame

Evening Treat: Gingerbread ice cream sandwich (fill 2 gingersnaps with one-half cup light vanilla ice cream)
Nutrition info for the day: 1,941 calories, 100g protein, 40g fat (5g sat), 293g carbs, 34g fiber

""")
    if age in range(31,40) :
            st.title("Key Nutrients You Need Now ")
            st.write("""Folate: It's critical for supporting a healthy pregnancy, preventing neural-tube defects and helping your body make new cells. Folate may also help reduce the risk of heart disease. Eat foods such as chickpeas, asparagus, spinach, broccoli, avocados, orange juice, and fortified whole grains to help meet your daily 400-microgram requirement.

Phytonutrients: "These compounds contain antioxidants, which slow the aging process, ward off heart disease, and prevent changes in DNA, potentially preventing the development of cancer," says Bonci. While phytonutrients come from plants, dark chocolate, red wine, and coffee are highest in them.

Iron: When you don't get enough iron, you might feel physically drained and mentally exhausted. Researchers at Penn State University found that young women who were deficient in the mineral took longer and performed worse on cognitive tasks than those who had normal levels of iron. Get your daily dose of 18 milligrams from foods such as clams, lean beef, fortified breakfast cereal, soybeans, pumpkin seeds, and skinless poultry.
            """)
            st.title("The Age Diet Chart for Your 30s")
            st.write("""Breakfast: Whole-wheat English muffin topped with 2 tablespoons natural peanut butter and 1/2 small sliced banana, and 1 cup calcium- and vitamin D-fortified orange juice

Morning Snack: 1/2 cup Cheerios with 1/2 cup 1-percent or nonfat milk

Lunch: Curried shrimp salad (boil 10 shrimp and mix with 1 tablespoon mayonnaise and 1 teaspoon curry powder) in a whole wheat pita, and 1 cup watermelon chunks

Afternoon Snack: 6-ounce container light yogurt with 1/2 cup raspberries

Dinner: Chickpea salad (toss 1/2 cup canned, drained chickpeas with 1 tablespoon Italian dressing), 4 ounces lean flank steak, grilled or broiled, topped with 2 tablespoons teriyaki sauce, 2 cups baby spinach sautéed in 1 teaspoon olive oil, and 1 medium baked sweet potato

Evening Treat: 1 ounce dark chocolate

Nutrition info for the day: 1,868 calories, 94g protein, 64g fat (17g sat), 243g carbs, 34g fiber """)
    if age in range(41,50):
           st.title("Key Nutrients You Need Now ")
           st.write("""Calcium: As you approach menopause, bone-building estrogen starts to decline and calcium becomes more important. Ironically, you absorb less calcium from the food you eat because your stomach doesn't make as much of the acid necessary for absorption. Aim for 1,000 milligrams a day from low-fat dairy, supplements, or a combination.

Vitamin D: This nutrient helps your body absorb calcium, keeps your immune system strong, protects against breast and colon cancers, and even prevents hearing loss. But by the time you reach your 40s, your vitamin D levels quickly start to plummet. "There's no way to get enough vitamin D from your diet because very few foods contain it," says Bonci. Your best bet: a daily supplement of 600 to 1,000 international units. (The FDA regulates supplements like food rather than drugs, i.e. less strictly. If you're thinking of taking a supplement, always check with your doctor first.)

Fiber: Fiber not only makes you feel fuller longer, but it also "helps decrease cholesterol and your risk for colon cancer," says Dr. Peeke. Try to eat a mix of soluble (from fruits, vegetables, barley, and oats) and insoluble (from whole-wheat bread and bran) fiber daily. """)
           st.title("The Age Diet Chart for Your 40s")
           st.write(""" Breakfast: 1 cup high-fiber cereal (such as bran flakes) with 1 cup 1-percent milk and 1 cup blueberries, and 1 cup green tea

Morning Snack: 1 medium apple with 1 tablespoon soy-nut butter

Lunch: Veggie burger on a whole wheat bun with 2 slices low-fat cheddar cheese (1 ounce each), and a 6-ounce can low-sodium vegetable juice

Afternoon Snack: 2 tablespoons hummus with 6 whole wheat crackers

Dinner: 3 ounces broiled salmon over 1 cup barley pilaf, and 6 asparagus spears sautéed in 1 teaspoon olive oil

Evening Treat: 6-ounce container light vanilla yogurt topped with 1 tablespoon mini chocolate chips

Nutrition info for the day: 1,656 calories, 92g protein, 48g fat (13g sat), 228g carbs, 39g fiber""")