# This is sample code created for illustration purposes only
# See: https://platform.openai.com/docs/assistants/overview for more information


assistant = client.beta.assistants.create(
    name="SoarNow Assistant",
    instructions="You are a concierge. Use the provided functions to answer questions and take actions for Young Bird Club members.",
    model="gpt-4-1106-preview",
    tools=[
        {
            "name": "scheduleAppointment",
            "description": "Arrange appointments between users by coordinating with their respective agents to find suitable times.",
            "parameters": {
                "userIDs": ["string"],
                "preferredDates": ["string"],
                "appointmentType": "string",
            },
        },
        {
            "name": "conferenceTicketReservation",
            "description": "Reserve tickets for conferences, including selecting sessions, workshops, and booking slots.",
            "parameters": {
                "conferenceID": "string",
                "userPreferences": "object",
                "paymentDetails": "object",
            },
        },
        {
            "name": "concertTicketPurchase",
            "description": "Assist users in buying tickets to concerts, including seat selection and payment processing.",
            "parameters": {
                "concertID": "string",
                "seatingPreferences": "object",
                "paymentDetails": "object",
            },
        },
        {
            "name": "partyFinderAndReservation",
            "description": "Help users discover parties during conferences and facilitate ticket reservations or guest list inclusion.",
            "parameters": {
                "conferenceID": "string",
                "userPreferences": "object",
                "partyDateTime": "string",
            },
        },
        {
            "name": "restaurantBooking",
            "description": "Book tables at restaurants, including special requests like dietary preferences or occasion.",
            "parameters": {
                "restaurantID": "string",
                "bookingDateTime": "string",
                "specialRequests": "object",
            },
        },
        {
            "name": "transportationArrangement",
            "description": "Arrange transportation for users, such as taxis, limousines, or ride-shares to various events or destinations.",
            "parameters": {
                "pickupLocation": "string",
                "destination": "string",
                "time": "string",
                "vehiclePreference": "string",
            },
        },
        {
            "name": "hotelAccommodationBooking",
            "description": "Find and book hotel rooms based on user preferences like location, budget, and amenities.",
            "parameters": {
                "city": "string",
                "checkInDate": "string",
                "checkOutDate": "string",
                "roomPreferences": "object",
            },
        },
        {
            "name": "personalItineraryCreation",
            "description": "Create personalized itineraries for users attending events, including time management for meetings, sessions, and social activities.",
            "parameters": {
                "eventIDs": ["string"],
                "userSchedule": "object",
                "preferences": "object",
            },
        },
        {
            "name": "exclusiveEventAccess",
            "description": "Gain access to exclusive events or VIP areas within conferences or concerts for users.",
            "parameters": {
                "eventID": "string",
                "userProfile": "object",
                "requiredAccessLevel": "string",
            },
        },
        {
            "name": "emergencyServicesContact",
            "description": "Quickly connect users with emergency services when required, such as medical, legal, or security assistance.",
            "parameters": {
                "emergencyType": "string",
                "userLocation": "string",
                "personalDetails": "object",
            },
        },
        {
            "name": "personalStylistConsultation",
            "description": "Arrange consultations with a personal stylist or fashion advisor for events.",
            "parameters": {
                "eventType": "string",
                "personalStyle": "string",
                "sizes": "object",
                "budget": "number",
            },
        },
        {
            "name": "privateEventPlanning",
            "description": "Assist in planning and executing private events.",
            "parameters": {
                "eventSize": "number",
                "theme": "string",
                "locationPreferences": "string",
                "cateringNeeds": "object",
            },
        },
        {
            "name": "exclusiveDealCuration",
            "description": "Curate and present exclusive deals and opportunities.",
            "parameters": {
                "interestAreas": ["string"],
                "investmentPreferences": "object",
                "riskProfile": "string",
            },
        },
        {
            "name": "networkingOpportunityMatcher",
            "description": "Connect members with similar or complementary interests for networking.",
            "parameters": {
                "professionalProfile": "object",
                "networkingGoals": "object",
                "industryInterests": ["string"],
            },
        },
        {
            "name": "luxuryCarRentalService",
            "description": "Provide rental services for luxury vehicles.",
            "parameters": {
                "carPreferences": "object",
                "rentalDuration": "string",
                "pickupLocation": "string",
                "dropOffLocation": "string",
            },
        },
        {
            "name": "yachtOrJetChartering",
            "description": "Facilitate the chartering of yachts or private jets.",
            "parameters": {
                "charterType": "string",
                "duration": "string",
                "destinations": ["string"],
                "amenities": "object",
            },
        },
        {
            "name": "personalShopperService",
            "description": "Connect users with personal shoppers to assist in purchasing and styling.",
            "parameters": {
                "shoppingPreferences": "object",
                "budget": "number",
                "personalStyle": "string",
            },
        },
        {
            "name": "exclusiveClubEventsNotification",
            "description": "Notify members of exclusive events.",
            "parameters": {"memberID": "string", "preferenceFilter": "object"},
        },
        {
            "name": "privateGuidedTours",
            "description": "Arrange private guided tours for members at destinations.",
            "parameters": {
                "destinationID": "string",
                "tourPreferences": "object",
                "languages": ["string"],
            },
        },
        {
            "name": "healthAndWellnessReservations",
            "description": "Book health and wellness appointments like spas, massages, or personal training sessions.",
            "parameters": {
                "serviceType": "string",
                "location": "string",
                "timePreferences": "string",
            },
        },
        {
            "name": "gourmetFoodAndWineConsulting",
            "description": "Provide consulting on gourmet food and wine selections.",
            "parameters": {
                "cuisineType": "string",
                "winePreferences": "object",
                "eventDetails": "object",
            },
        },
        {
            "name": "VIPAccessAndExperienceEnhancement",
            "description": "Enhance the user's experience at events with VIP access and exclusive services.",
            "parameters": {"eventID": "string", "VIPPreferences": "object"},
        },
        {
            "name": "artAcquisitionAssistance",
            "description": "Assist members in the acquisition of art, including connecting with galleries and arranging viewings.",
            "parameters": {
                "artType": "string",
                "artistPreferences": ["string"],
                "budget": "number",
            },
        },
        {
            "name": "securityDetailArrangement",
            "description": "Arrange personal security details for members.",
            "parameters": {
                "securityLevel": "string",
                "duration": "string",
                "specificRequirements": "object",
            },
        },
    ],
)
