import React from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
  StatusBar,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';

export default function TabsIndex() {
  const router = useRouter();

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#f8fafc" />
      
      <View style={styles.container}>
        {/* Header */}
        <View style={styles.header}>
          <View style={styles.logoContainer}>
            <Ionicons name="medical" size={32} color="#1E40AF" />
            <View style={styles.headerTextContainer}>
              <Text style={styles.headerTitle}>E-Aarogya</Text>
              <Text style={styles.headerSubtitle}>Health Surveillance System</Text>
            </View>
          </View>
        </View>

        {/* Navigation Cards */}
        <View style={styles.content}>
          <Text style={styles.sectionTitle}>Health Monitoring Dashboard</Text>
          
          {/* Live Disease Tracker */}
          <TouchableOpacity 
            style={styles.navCard}
            onPress={() => router.push('/outbreak-alert/livetracker' as any)}
            activeOpacity={0.7}
          >
            <View style={styles.navCardHeader}>
              <View style={[styles.navIcon, { backgroundColor: '#DBEAFE' }]}>
                <Ionicons name="analytics" size={28} color="#1E40AF" />
              </View>
              <View style={styles.navInfo}>
                <Text style={styles.navTitle}>Live Disease Tracker</Text>
                <Text style={styles.navSubtitle}>Real-time monitoring & GPS tracking</Text>
              </View>
              <Ionicons name="chevron-forward" size={24} color="#9CA3AF" />
            </View>
          </TouchableOpacity>

          {/* Outbreak Details */}
          <TouchableOpacity 
            style={styles.navCard}
            onPress={() => router.push('/outbreak-alert/outbreakdetails' as any)}
            activeOpacity={0.7}
          >
            <View style={styles.navCardHeader}>
              <View style={[styles.navIcon, { backgroundColor: '#FEE2E2' }]}>
                <Ionicons name="warning" size={28} color="#DC2626" />
              </View>
              <View style={styles.navInfo}>
                <Text style={styles.navTitle}>Outbreak Details</Text>
                <Text style={styles.navSubtitle}>Comprehensive outbreak information</Text>
              </View>
              <Ionicons name="chevron-forward" size={24} color="#9CA3AF" />
            </View>
          </TouchableOpacity>

          {/* Safety Tips */}
          <TouchableOpacity 
            style={styles.navCard}
            onPress={() => router.push('/outbreak-alert/safetytips' as any)}
            activeOpacity={0.7}
          >
            <View style={styles.navCardHeader}>
              <View style={[styles.navIcon, { backgroundColor: '#D1FAE5' }]}>
                <Ionicons name="shield-checkmark" size={28} color="#059669" />
              </View>
              <View style={styles.navInfo}>
                <Text style={styles.navTitle}>Safety Tips & Guidelines</Text>
                <Text style={styles.navSubtitle}>Prevention & emergency procedures</Text>
              </View>
              <Ionicons name="chevron-forward" size={24} color="#9CA3AF" />
            </View>
          </TouchableOpacity>

          {/* Main Dashboard */}
          <TouchableOpacity 
            style={styles.navCard}
            onPress={() => router.push('/outbreak-alert' as any)}
            activeOpacity={0.7}
          >
            <View style={styles.navCardHeader}>
              <View style={[styles.navIcon, { backgroundColor: '#F3E8FF' }]}>
                <Ionicons name="apps" size={28} color="#7C3AED" />
              </View>
              <View style={styles.navInfo}>
                <Text style={styles.navTitle}>Full Dashboard</Text>
                <Text style={styles.navSubtitle}>Complete health monitoring interface</Text>
              </View>
              <Ionicons name="chevron-forward" size={24} color="#9CA3AF" />
            </View>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#f8fafc',
    paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 0,
  },
  container: {
    flex: 1,
  },
  header: {
    paddingHorizontal: 20,
    paddingVertical: 16,
    backgroundColor: '#ffffff',
    borderBottomWidth: 1,
    borderBottomColor: '#e5e7eb',
  },
  logoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  headerTextContainer: {
    flex: 1,
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1F2937',
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#6B7280',
    marginTop: 2,
  },
  content: {
    flex: 1,
    padding: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    color: '#1F2937',
    marginBottom: 20,
  },
  navCard: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  navCardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  navIcon: {
    width: 56,
    height: 56,
    borderRadius: 28,
    justifyContent: 'center',
    alignItems: 'center',
  },
  navInfo: {
    flex: 1,
  },
  navTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#1F2937',
  },
  navSubtitle: {
    fontSize: 14,
    color: '#6B7280',
    marginTop: 2,
  },
});
