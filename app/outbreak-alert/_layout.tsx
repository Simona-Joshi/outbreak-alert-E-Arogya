import { Stack } from 'expo-router';

export default function OutbreakAlertLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: false,
      }}
    >
      <Stack.Screen
        name="index"
        options={{
          title: 'E-Aarogya',
        }}
      />
      <Stack.Screen
        name="livetracker"
        options={{
          title: 'Live Disease Tracker',
          presentation: 'modal',
        }}
      />
      <Stack.Screen
        name="outbreakdetails"
        options={{
          title: 'Outbreak Details',
          presentation: 'modal',
        }}
      />
      <Stack.Screen
        name="safetytips"
        options={{
          title: 'Safety Tips',
          presentation: 'modal',
        }}
      />
    </Stack>
  );
}
